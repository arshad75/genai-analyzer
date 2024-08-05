```go
package main

import (
	"context"
	"fmt"
	"io"
	"log"
	"os"

	dialogflow "cloud.google.com/go/dialogflow/apiv2"
	"cloud.google.com/go/dialogflow/apiv2/dialogflowpb"
	"github.com/GoogleCloudPlatform/golang-samples/dialogflow/v2/no-context"
	speech "cloud.google.com/go/speech/apiv1"
	speechpb "cloud.google.com/go/speech/apiv1/speechpb"
)

func main() {
	ctx := context.Background()

	// Sets your Google Cloud Platform project ID
	projectID := nocontext.ProjectID
	if projectID == "" {
		log.Fatal("Google Cloud Platform project ID not set")
	}

	// Creates a client
	sessionsClient, err := dialogflow.NewSessionsClient(ctx)
	if err != nil {
		log.Fatalf("Failed to create sessions client: %v", err)
	}

	// Sets the session name using the projectID (my-project-id) and sessionId (UUID)
	sessionPath := fmt.Sprintf("projects/%s/agent/sessions/%s", projectID, nocontext.SessionID)

	// Detects speech using microphone
	stream, err := speech.NewClient(ctx).Recognize(ctx)
	if err != nil {
		log.Fatalf("Failed to create speech client: %v", err)
	}

	go func() {
		buf := make([]byte, 16000)
		for {
			n, err := os.Stdin.Read(buf)
			if err != nil {
				log.Printf("Error while reading from microphone: %v", err)
				stream.CloseSend()
				return
			}
			err = stream.Send(&speechpb.StreamingRecognizeRequest{
				AudioContent: buf[:n],
			})
			if err != nil {
				log.Fatalf("Could not send audio: %v", err)
			}
		}
	}()

	for {
		resp, err := stream.Recv()
		if err == io.EOF {
			stream.CloseSend()
			break
		}
		if err != nil {
			log.Fatalf("Cannot stream results: %v", err)
		}

		if err := sendText(ctx, sessionsClient, sessionPath, resp.Results[0].Alternatives[0].Transcript); err != nil {
			log.Fatalf("Could not send %q: %v", resp.Results[0].Alternatives[0].Transcript, err)
		}
	}
}

func sendText(ctx context.Context, sessionsClient *dialogflow.SessionsClient, sessionPath string, text string) error {
	queryText := dialogflowpb.QueryInput_Text{
		Text: &dialogflowpb.TextInput{
			Text: text,
		},
	}
	queryInput := dialogflowpb.QueryInput{
		Input: &queryText,
	}
	req := &dialogflowpb.DetectIntentRequest{
		Session: sessionPath,
		QueryInput: &queryInput,
		// Optional. The language used by the client application.
		// If not specified, the Assistant will use the project's default language code.
		// For more information, see https://cloud.google.com/dialogflow/docs/reference/language
		LanguageCode: "en-US",
	}
	resp, err := sessionsClient.DetectIntent(ctx, req)
	if err != nil {
		return err
	}
	fmt.Println(resp.GetQueryResult().GetFulfillmentText())
	return nil
}
```
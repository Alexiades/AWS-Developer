from typing import Text
import boto3
#Explicit Client Configuratio, insert your own Access Keys Credentials
polly = boto3.client('polly',
                      region_name='us-west-2',
                      aws_access_key_id='',
                      aws_secret_access_key=''
                      )

#Implicit Client Configuration
polly = boto3.client('polly')

result = polly.synthesize_speech(Text='Hello World!',
OutputFormat='mp3',
VoiceId='Aditi')

# Save the Audio from the response
audio = result['AudioStream'].read()
with open("helloworld.mp3","wb") as file:
    file.write(audio)

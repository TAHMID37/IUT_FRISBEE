# IUT_FRISBEE


Clone repository

Downlaod the model.zip file and extract it, copy the model folder in the project directory.
[Team_IUT_FRISBEE_ONE_DRIVE](https://iutdhaka-my.sharepoint.com/:f:/g/personal/rafihassan_iut-dhaka_edu/EnaPmHUz0S9PidqCe60lp-EBFKEktdRZknUS70BmASLB4g?e=ysmI2f)



Create a  .env file and fill it with same variables from env.txt and update the variables.

Create a virtual environment:
`py -3.11 -m venv env`
`env\Scripts\activate`

Run these commands:
`pip install -r requirements.txt`
`uvicorn app.main:app`

### FrontEnd

You have to install node.js before starting the app

To start frontend, go to the 'client/meeting_minute-app/' directory and run `npm i`. After installing dependencies run `npm start`.
<!-- You have to install node.js before starting the app and install the following libraries:
`npm install bootstrap`
`npm install react-spinners`
`npm install react-markdown` -->


### Troubleshooting

- **FFmpeg Issue:**
  If you encounter an error related to FFmpeg not being found while loading audio files, you can resolve it by following the steps outlined [here](https://discuss.huggingface.co/t/audio-classification-pipeline-valueerror-ffmpeg-was-not-found-but-is-required-to-load-audio-files-from-filename/16137/7).

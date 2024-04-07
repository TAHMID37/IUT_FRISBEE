import React, { useState } from "react";
import api from "../api";
import Navbar from "./Navbar";

import { css } from "@emotion/react";
import { BarLoader } from "react-spinners";

const AudioUploaderBangla = () => {
  const [file, setFile] = useState(null);
  const [fileName, setFileName] = useState("");
  const [transcription, setTranscription] = useState("");
  const [meetingMinutesResponse, setMeetingMinutesResponse] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);
  const [dragOver, setDragOver] = useState(false);

  const override = css`
    display: block;
    margin: 0 auto;
    border-color: red;
  `;

  const getSummary = (response) => {
    const startIndex = response.indexOf("Summary:");
    const endIndex = response.indexOf("Crucial Deadline:");
    return response.substring(startIndex + 9, endIndex).trim();
  };

  const getDeadline = (response) => {
    const startIndex = response.indexOf("Crucial Deadline:");
    const endIndex = response.indexOf("Follow-up actions:");
    return response.substring(startIndex + 17, endIndex).trim();
  };

  const getFollowUpActions = (response) => {
    const startIndex = response.indexOf("Follow-up actions:");
    return response.substring(startIndex + 18).trim();
  };

  const handleFileChange = (event) => {
    const selectedFile = event.target.files[0];
    setFile(selectedFile);
    setFileName(selectedFile ? selectedFile.name : "");
  };

  const handleDragEnter = (event) => {
    event.preventDefault();
    setDragOver(true);
  };

  const handleDragOver = (event) => {
    event.preventDefault();
    setDragOver(true);
  };

  const handleDragLeave = (event) => {
    event.preventDefault();
    setDragOver(false);
  };

  const handleDrop = (event) => {
    event.preventDefault();
    setDragOver(false);
    const droppedFile = event.dataTransfer.files[0];
    setFile(droppedFile);
    setFileName(droppedFile ? droppedFile.name : "");
  };

  const handleSubmit = async () => {
    try {
      if (!file) {
        throw new Error("Please select a file to upload");
      }

      setLoading(true);

      const formData = new FormData();
      formData.append("file", file);

      const response = await api.post("/upload_bangla/", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });

      if (response.status !== 200) {
        throw new Error("Failed to upload audio file");
      }

      const data = response.data;
      setTranscription(data.transcription);

      const meetingMinutesResponse = await api.post("/bangla_meeting_minutes", {
        text: data.transcription.text,
      });

      if (meetingMinutesResponse.status !== 200) {
        throw new Error("Failed to send meeting minutes");
      }

      setMeetingMinutesResponse(meetingMinutesResponse.data); // Set meeting minutes response
    } catch (error) {
      setError(error.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <Navbar />
      <div
        style={{ marginTop: "20px" }}
        className={`container center ${dragOver ? "drag-over" : ""}`}
      >
        <div class="row">
          <div class="col-md-12">
            <h1 class="white">Bangla</h1>
            <p class="white"></p>
          </div>
        </div>
        <form
          name="upload"
          method="post"
          action="#"
          enctype="multipart/form-data"
          accept-charset="utf-8"
        >
          <div
            className="row"
            onDragEnter={handleDragEnter}
            onDragOver={handleDragOver}
            onDragLeave={handleDragLeave}
            onDrop={handleDrop}
          >
            <div class="col-md-12 col-md-offset-3 center">
              <div class="btn-container">
                <input
                  type="file"
                  id="fileInput"
                  accept="audio/*"
                  onChange={handleFileChange}
                  style={{ display: "none" }}
                />
                <label htmlFor="fileInput" className="drop-area ">
                  <p>
                    {fileName
                      ? `Selected File: ${fileName}`
                      : "Click to select or drop file here"}
                  </p>
                  <button
                    type="button"
                    class="btn btn-primary btn-lg"
                    onClick={() => document.getElementById("fileInput").click()}
                  >
                    Browse for your Audio File!
                  </button>
                </label>
              </div>
            </div>
          </div>

          <div className="row">
            <div className="col-md-12">
              <button
                type="button"
                className="btn btn-default"
                onClick={handleSubmit}
                disabled={loading}
                style={{
                  color: "#ffffff",
                  backgroundColor: "transparent",
                  borderColor: "#ffffff",
                }}
              >
                Upload Audio
              </button>
            </div>
          </div>
          
        </form>
        <br></br>
        <div class="row">
          <div class="col-md-12">
            <h1 class="white">Meeting audio text output</h1>
            <p class="white"></p>
          </div>

          <div className="col-md-12 col-md-offset-3 center">
            <div className="btn-container">
              <div className="loader-container">
                <br></br>
                <BarLoader
                  color={"#123abc"}
                  loading={loading}
                  css={override}
                  className="loader"
                />
              </div>
              {!transcription.text && !error && <p>Your Output will be here</p>}
              {transcription.text && <p>Transcription: {transcription.text}</p>}
              {error && <p>Error: {error}</p>}
              {meetingMinutesResponse && (
                <div>
                  <p>
                    <strong>Summary:</strong>{" "}
                    {getSummary(meetingMinutesResponse)}
                  </p>
                  <p>
                    <strong>Crucial Deadline:</strong>{" "}
                    {getDeadline(meetingMinutesResponse)}
                  </p>
                  <p>
                    <strong>Follow-up actions:</strong>{" "}
                    {getFollowUpActions(meetingMinutesResponse)}
                  </p>
                </div>
              )}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default AudioUploaderBangla;

# Crowd Detection and Logging in Videos

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Overview

This repository contains a Python-based system for detecting and logging crowds of people within videos. It leverages the YOLOv3 object detection model to identify individuals and the DBSCAN clustering algorithm to determine if groups of people constitute a crowd. The system then records instances of crowd formation, along with relevant data, into a CSV log file.

This is useful in areas like:

*   **Traffic monitoring:** check the density of people in an area.
*   **Security:** detect large group of people in restricted areas.
*   **Retail:** analyze customer patterns.
* **Events:** to make sure there is no overcrowding.

## Features

*   **Person Detection:** Employs the pre-trained YOLOv3 model for robust person detection in video frames.
*   **Crowd Clustering:** Uses the DBSCAN algorithm to identify groups of nearby people, indicating crowd formation.
*   **Consecutive Frame Analysis:** Only logs crowd occurrences if they persist for 10 consecutive video frames, reducing false positives.
*   **CSV Output:**  Logs crowd-related data (frame number, maximum crowd size) to a structured CSV file (`crowd_log.csv`).
*   **Automatic Model Download:** Automatically downloads the necessary YOLOv3 weights and configuration files if they are not present.
* **Dummy Video:** Creates a dummy video if the user does not have one, for testing.

## Getting Started

### Prerequisites

*   Python 3.7+
*   The following Python libraries:
    *   `opencv-python`
    *   `numpy`
    *   `pandas`
    *   `scikit-learn`
    * `wget`
    * `ffmpeg` (if the user does not have a video for testing)

### Installation

1.  Clone this repository:

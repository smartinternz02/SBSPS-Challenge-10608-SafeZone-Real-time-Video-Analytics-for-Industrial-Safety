# SafeZone: Real-time Video Analytics for Industrial Safety

![safezone_icon](https://github.com/smartinternz02/SBSPS-Challenge-10608-SafeZone-Real-time-Video-Analytics-for-Industrial-Safety/assets/76390896/bb399e5b-6310-4411-999c-47823b86fc0c)


## Overview

SafeZone is an innovative real-time video analytics web application developed to enhance workplace safety in industrial environments. By leveraging a combination of Flask, YOLO, HTML, CSS, JavaScript, Bootstrap, OpenCV, and IBM Watson Assistant, SafeZone detects potential hazards like weapons, falls, and person with robber-mask. The system provides swift alerts to users and offers assistance through interactive chatbots.

## Features

- **Real-time Hazard Detection:** Utilizes YOLO (You Only Look Once) object detection model to identify potential hazards in real-time.
- **Interactive Chatbot Integration:** Employs IBM Watson Assistant to provide users with immediate guidance and information.
- **Email Alert Mechanism:** Sends timely email alerts to users, containing relevant attachments such as detected images or video frames.
- **Proactive Prevention:** Detects hazards as they occur, enabling organizations to take preventive measures and enhance workplace safety.
- **Multi-Class Detection:** Trained YOLO model to recognize three distinct classes: weapon detection, fall-detection, and robber-mask detection.

## Usage

1. Run the application: `python app.py`
2. Access the application via your web browser at `http://localhost:5000`

## Screenshots
**1) Home Page**

![image](https://github.com/smartinternz02/SBSPS-Challenge-10608-SafeZone-Real-time-Video-Analytics-for-Industrial-Safety/assets/76390896/f32fd016-e436-4ba9-8777-3c44b9b1cc99)

**2) Try Us Page**

![image](https://github.com/smartinternz02/SBSPS-Challenge-10608-SafeZone-Real-time-Video-Analytics-for-Industrial-Safety/assets/76390896/2540b981-c13d-449c-a417-ebf1019d46ed)
**3) About Us Page**

![image](https://github.com/smartinternz02/SBSPS-Challenge-10608-SafeZone-Real-time-Video-Analytics-for-Industrial-Safety/assets/76390896/13c95fd4-ffaf-4792-9ad4-def6238920a4)
**4) Creators Page**

![image](https://github.com/smartinternz02/SBSPS-Challenge-10608-SafeZone-Real-time-Video-Analytics-for-Industrial-Safety/assets/76390896/0ab26ef5-caa2-41b7-916d-4c3df122594e)
**5) Contact-Us Page**

![image](https://github.com/smartinternz02/SBSPS-Challenge-10608-SafeZone-Real-time-Video-Analytics-for-Industrial-Safety/assets/76390896/5dee3201-7d55-4b20-a77c-277fe1e88a00)

## Detection Screenshot/Video

**1) Detection Video of Gun**

![20230828_002746](https://github.com/smartinternz02/SBSPS-Challenge-10608-SafeZone-Real-time-Video-Analytics-for-Industrial-Safety/assets/76390896/dbb9cd02-a719-483a-b7ea-4eb1cd6ef465)

**2) Detection Video of person fall**

![20230828_003119](https://github.com/smartinternz02/SBSPS-Challenge-10608-SafeZone-Real-time-Video-Analytics-for-Industrial-Safety/assets/76390896/eceba4f6-3446-4be3-bc04-1e15d7ddf957)

**3) Detection of Robbery-Mask**

![robbery](https://github.com/smartinternz02/SBSPS-Challenge-10608-SafeZone-Real-time-Video-Analytics-for-Industrial-Safety/assets/76390896/bb159bd0-0098-428a-90b0-5a088d51a15a)

## Working Screenshot

**1) User Uploaded Video And Frame are Been Analysed**

![image](https://github.com/smartinternz02/SBSPS-Challenge-10608-SafeZone-Real-time-Video-Analytics-for-Industrial-Safety/assets/76390896/85fbd27d-1770-47ee-b2bd-eab195ca64e2)
**2) Web Page Pop Warning Message And User Can Download The Video And Video Contain Only Those Frame Where Detection Occured**

![image](https://github.com/smartinternz02/SBSPS-Challenge-10608-SafeZone-Real-time-Video-Analytics-for-Industrial-Safety/assets/76390896/90c556b4-a10d-49ba-aba9-e3a16b2f5b9e)
**3) User Is Alerted Via Gmail And Message Contain Attachment Video Of Detected Hazards**

![image](https://github.com/smartinternz02/SBSPS-Challenge-10608-SafeZone-Real-time-Video-Analytics-for-Industrial-Safety/assets/76390896/586308df-af6b-4a0a-9d24-8e69e72211b5)
**4) If User Upload Image In Web Page And Image Contain Any Potential Issue The Alert Is Send To User With Attached Detected Image And Bounding Box Is Drawn On Image**

![image](https://github.com/smartinternz02/SBSPS-Challenge-10608-SafeZone-Real-time-Video-Analytics-for-Industrial-Safety/assets/76390896/47d55161-8e6b-4e6d-a0eb-fcf72b67fd6b)
**5) User Uploading Image**

![image](https://github.com/smartinternz02/SBSPS-Challenge-10608-SafeZone-Real-time-Video-Analytics-for-Industrial-Safety/assets/76390896/0d299804-6525-472c-8357-26b46e540956)
**6) No Issue Detected As Uploaded Image Does Contain Any Harmful Object**

![image](https://github.com/smartinternz02/SBSPS-Challenge-10608-SafeZone-Real-time-Video-Analytics-for-Industrial-Safety/assets/76390896/1cc0e0a3-ed3e-4001-aa0a-00c9a7c4cbba)

**7) User Chatting with IBM Watson Chatbot**

![image](https://github.com/smartinternz02/SBSPS-Challenge-10608-SafeZone-Real-time-Video-Analytics-for-Industrial-Safety/assets/76390896/81411385-72f7-494d-ade6-243184f5dc82)

## Team Members

1. Suryansh Sharma
   - Course 1: [Journey to Cloud: Envisioning Your Solution](https://www.credly.com/badges/091a5170-2e31-499c-9e44-d8eaa8f4da09/public_url)
   - Course 2: [Getting Started with Enterprise-grade AI](https://www.credly.com/badges/a09f302a-eefb-4bad-91ef-2fce73ad0bf7/public_url)

2. Aditya Bawnoo
   - Course 1: [Journey to Cloud: Envisioning Your Solution](https://www.credly.com/badges/d8a9c19d-75fc-4b9e-9a93-4674c9a3a79c/public_url)
   - Course 2: [Getting Started with Enterprise-grade AI](https://www.credly.com/badges/9550b76c-476e-4953-80e2-d4d9728576b1/public_url)

3. Sanidhya Sharma
   - Course 1: [Journey to Cloud: Envisioning Your Solution](https://www.credly.com/badges/4a09ba7a-d569-45f2-83f9-839d503df0b3/public_url)
   - Course 2: [Getting Started with Enterprise-grade AI](https://www.credly.com/badges/4df2d1a7-df81-4976-960f-5f2d8bbb715d/public_url)

3. Aryan Sharma
   - Course 1: [Journey to Cloud: Envisioning Your Solution](https://www.credly.com/badges/4a09ba7a-d569-45f2-83f9-839d503df0b3/public_url)
   - Course 2: [Getting Started with Enterprise-grade AI](https://www.credly.com/badges/4df2d1a7-df81-4976-960f-5f2d8bbb715d/public_url)



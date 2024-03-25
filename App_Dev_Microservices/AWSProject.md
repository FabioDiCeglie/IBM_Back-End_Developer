## Introduction
Let’s build a simple serverless application using AWS Lambda.

This application will have an html front end hosted on AWS Amplify, where you can enter some text. On submitting the form, it will provide you with a response which is capitalized and reverse of your entered text.

Capitalize and Reverse will be two separate Lambda functions to show you the chaining capabilities. Instead of accessing these functions directly, an API Gateway will be used to accept client requests and respond with the final output.
- AWS CodeCommit
- AWS Amplify
- AWS Lambda Functions
- AWS Step Function
- AWS API Gateway

## Process
<img width="1065" alt="Screenshot 2024-03-25 at 17 40 47" src="https://github.com/FabioDiCeglie/IBM_Back-End_Developer/assets/93951206/da741ac1-d938-484e-b9fa-5c7018fc132d">
<img width="944" alt="Screenshot 2024-03-25 at 17 40 58" src="https://github.com/FabioDiCeglie/IBM_Back-End_Developer/assets/93951206/a3c81343-2158-40f4-89b8-78f28131de6c">
<img width="1048" alt="Screenshot 2024-03-25 at 17 41 06" src="https://github.com/FabioDiCeglie/IBM_Back-End_Developer/assets/93951206/bf70e343-dd1f-4917-9fac-6b33a610994f">
<img width="928" alt="Screenshot 2024-03-25 at 17 41 14" src="https://github.com/FabioDiCeglie/IBM_Back-End_Developer/assets/93951206/2901f737-6d8e-4efa-8838-780ac1757747">
<img width="897" alt="Screenshot 2024-03-25 at 17 41 22" src="https://github.com/FabioDiCeglie/IBM_Back-End_Developer/assets/93951206/2e99395f-1a6d-4407-acc4-9020f9d1b234">
<img width="928" alt="Screenshot 2024-03-25 at 17 41 31" src="https://github.com/FabioDiCeglie/IBM_Back-End_Developer/assets/93951206/e7f419d2-aab6-429d-85dc-4fb882bb8b6f">
<img width="931" alt="Screenshot 2024-03-25 at 17 41 38" src="https://github.com/FabioDiCeglie/IBM_Back-End_Developer/assets/93951206/656e7733-dd61-431c-bc08-bc7d46b61b31">
<img width="893" alt="Screenshot 2024-03-25 at 17 41 47" src="https://github.com/FabioDiCeglie/IBM_Back-End_Developer/assets/93951206/4b163491-437a-4656-85a9-c1b41156332a">
<img width="933" alt="Screenshot 2024-03-25 at 17 41 56" src="https://github.com/FabioDiCeglie/IBM_Back-End_Developer/assets/93951206/6e545ea0-0593-4f69-8ee6-0a6370023441">
<img width="924" alt="Screenshot 2024-03-25 at 17 42 05" src="https://github.com/FabioDiCeglie/IBM_Back-End_Developer/assets/93951206/a8fd25c2-8ab0-49fe-a296-13f161b9a9e4">
<img width="949" alt="Screenshot 2024-03-25 at 17 42 12" src="https://github.com/FabioDiCeglie/IBM_Back-End_Developer/assets/93951206/f0e936de-5cd7-40a4-833a-e9b4908d3b55">
<img width="896" alt="Screenshot 2024-03-25 at 17 42 20" src="https://github.com/FabioDiCeglie/IBM_Back-End_Developer/assets/93951206/fa31c01e-1dc3-475c-8425-9a05d35cf4b1">
<img width="892" alt="Screenshot 2024-03-25 at 17 42 38" src="https://github.com/FabioDiCeglie/IBM_Back-End_Developer/assets/93951206/54e6f76d-ea87-4460-b325-851d9a1a9aa3">
<img width="876" alt="Screenshot 2024-03-25 at 17 42 46" src="https://github.com/FabioDiCeglie/IBM_Back-End_Developer/assets/93951206/edbd8d19-04ce-4c4d-afdc-614052983411">
<img width="465" alt="Screenshot 2024-03-25 at 17 43 01" src="https://github.com/FabioDiCeglie/IBM_Back-End_Developer/assets/93951206/854f86ef-06ea-4632-a4ff-4281dfbbf55f">
<img width="599" alt="Screenshot 2024-03-25 at 17 43 18" src="https://github.com/FabioDiCeglie/IBM_Back-End_Developer/assets/93951206/04ab8027-726e-4f92-848d-ee43c8585969">
<img width="527" alt="Screenshot 2024-03-25 at 17 43 25" src="https://github.com/FabioDiCeglie/IBM_Back-End_Developer/assets/93951206/b2645851-a68d-4ee4-b595-d614fea5940e">
<img width="521" alt="Screenshot 2024-03-25 at 17 43 31" src="https://github.com/FabioDiCeglie/IBM_Back-End_Developer/assets/93951206/f3934214-380e-4cf2-91f9-17600bae87d5">
<img width="481" alt="Screenshot 2024-03-25 at 17 43 39" src="https://github.com/FabioDiCeglie/IBM_Back-End_Developer/assets/93951206/cd9ab441-9fdc-4d4b-9ad5-f7f31afd51c6">
<img width="525" alt="Screenshot 2024-03-25 at 17 43 48" src="https://github.com/FabioDiCeglie/IBM_Back-End_Developer/assets/93951206/096814a4-250c-4b8a-9fc0-e9a04129bb07">
<img width="326" alt="Screenshot 2024-03-25 at 17 43 57" src="https://github.com/FabioDiCeglie/IBM_Back-End_Developer/assets/93951206/10eb2480-ba9a-4412-9496-1f8083c69dd6">
<img width="335" alt="Screenshot 2024-03-25 at 17 44 19" src="https://github.com/FabioDiCeglie/IBM_Back-End_Developer/assets/93951206/c99bc73e-3388-441f-90ea-03b77bfd4688">
<img width="439" alt="Screenshot 2024-03-25 at 17 44 08" src="https://github.com/FabioDiCeglie/IBM_Back-End_Developer/assets/93951206/047d6b46-b2eb-4d69-9f61-0ac340113974">


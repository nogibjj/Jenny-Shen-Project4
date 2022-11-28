# Jenny-Shen-Project4
[![Python application test with Github Actions](https://github.com/nogibjj/Jenny-Shen-Project4/actions/workflows/devops.yml/badge.svg)](https://github.com/nogibjj/Jenny-Shen-Project4/actions/workflows/devops.yml)

## Background, dataset and setups
Project 4 demonstrates how to create a Microservice by defining functions using yfinance API and using FastAPI. The source code is tested and pushed to Github and perform Continuous Integration with Github Actions. Last, we configure Build Server to Deploy Changes on build.

![images](https://user-images.githubusercontent.com/112578566/204195542-0aab28f6-b274-4e77-b3b2-d08a434b0500.png)


## Command Line Result

<img width="620" alt="Screen Shot 2022-11-27 at 11 34 05 PM" src="https://user-images.githubusercontent.com/112578566/204194739-f9278b1e-2b9c-481c-8b16-f20887a5bc4d.png">

<img width="465" alt="Screen Shot 2022-11-27 at 11 33 52 PM" src="https://user-images.githubusercontent.com/112578566/204194713-bf1977e4-636c-4290-bb61-d02dd0475e0f.png">

**1. Defined function that return the sector of a specific ticker**

<img width="706" alt="Screen Shot 2022-11-27 at 11 35 34 PM" src="https://user-images.githubusercontent.com/112578566/204194887-6601f0e9-2942-4341-ba27-b5a0c049bc35.png">
<img width="216" alt="Screen Shot 2022-11-27 at 11 35 42 PM" src="https://user-images.githubusercontent.com/112578566/204194899-13fa580d-9b8c-415c-a415-57703e37becf.png">

<img width="710" alt="Screen Shot 2022-11-27 at 11 36 02 PM" src="https://user-images.githubusercontent.com/112578566/204194927-c747feeb-a6e9-445f-9c2e-bd79c29c2c7a.png">
<img width="292" alt="Screen Shot 2022-11-27 at 11 36 11 PM" src="https://user-images.githubusercontent.com/112578566/204194938-39f044c2-1955-4d4c-8c5f-6a60088249de.png">

**2. Defined function that return the financial indicators of a specific ticker**

<img width="819" alt="Screen Shot 2022-11-27 at 11 32 07 PM" src="https://user-images.githubusercontent.com/112578566/204194560-5d983cac-6cd9-4a36-aabc-c0202f890258.png">
<img width="1493" alt="Screen Shot 2022-11-27 at 11 32 33 PM" src="https://user-images.githubusercontent.com/112578566/204194596-e449f517-77fb-4d9b-916b-ab646f6e902d.png">

Some financial information including EBIT and Net Income, which are usaully important indicator for investors to make decisions.

## Continuous Delivery
**1. Elastic Container Registry**

Creat a repository and copy all the push commands under to Deploy part of the MakeFile.

<img width="796" alt="Screen Shot 2022-11-27 at 11 38 02 PM" src="https://user-images.githubusercontent.com/112578566/204195114-b3a74354-01ac-46d0-ba8a-c3472ce3286b.png">

<img width="1011" alt="Screen Shot 2022-11-27 at 11 38 18 PM" src="https://user-images.githubusercontent.com/112578566/204195150-3f4afa6f-39c1-4048-bfc6-17694abc0cae.png">

**2. CodeBuild**

Creat a build project and try build to ensure the build process is successful.

<img width="1164" alt="Screen Shot 2022-11-27 at 11 38 50 PM" src="https://user-images.githubusercontent.com/112578566/204195191-9188a8fe-575c-4924-bc3f-f59005fab716.png">

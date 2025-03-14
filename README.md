# Safaricom Backend (Django)

![Python](https://img.shields.io/badge/Python-3.12-blue.svg)
![Django](https://img.shields.io/badge/Django-4.2.7-green.svg)
![DRF](https://img.shields.io/badge/DRF-3.14.0-orange.svg)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-lightblue.svg)
![Docker](https://img.shields.io/badge/Docker-Enabled-blue.svg)

## Overview

This is the backend component of a full-stack application developed for the Safaricom Ethiopia Integration Engineer exam. Built with **Django** and **Django REST Framework (DRF)**, it provides a robust API for managing bank-related KYC (Know Your Customer) data. The application is containerized using **Docker** and uses **PostgreSQL** as the database, ensuring scalability and ease of deployment.

The backend supports user authentication (via Django admin), data storage for banks, branches, and applications, and file uploads for proof of bank account documents. It exposes three key API endpoints to integrate with a React frontend.

---

## Features

- **API Endpoints**:
  - `GET /api/banks/`: Retrieve a list of banks.
  - `GET /api/branches/?bank_id={id}`: Retrieve branches for a specific bank.
  - `POST /api/applications/submit/`: Submit a KYC application with file upload.
- **Database**: PostgreSQL for persistent storage of banks, branches, and applications.
- **File Uploads**: Supports PDF, PNG, and JPG uploads for proof of bank account.
- **Dockerized**: Fully containerized with Docker and Docker Compose for consistent deployment.
- **Admin Interface**: Django admin panel for managing data (accessible at `/admin/`).

---

## Prerequisites

To run this project, ensure you have the following installed:
- [Docker Desktop](https://www.docker.com/products/docker-desktop) (Windows/Mac/Linux)
- [Git](https://git-scm.com/downloads)
- A web browser or API client (e.g., [Postman](https://www.postman.com/downloads/)) for testing

---

## Project Structure

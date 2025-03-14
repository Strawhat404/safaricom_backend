# Safaricom Backend (Django)

![Python](https://img.shields.io/badge/Python-3.12-blue.svg)
![Django](https://img.shields.io/badge/Django-4.2.7-green.svg)
![DRF](https://img.shields.io/badge/DRF-3.14.0-orange.svg)
![SQLite](https://img.shields.io/badge/SQLite-Default-lightgrey.svg)

## Overview

This is the backend for a full-stack application developed for the Safaricom Ethiopia Integration Engineer exam. Built with **Django** and **Django REST Framework (DRF)**, it provides APIs for a KYC (Know Your Customer) system, managing banks, branches, and applications. It uses **SQLite** as the default database for local development and supports file uploads for proof of bank account documents.

## Features

- **API Endpoints**:
  - `GET /api/banks/`: List all banks.
  - `GET /api/branches/?bank_id={id}`: List branches for a bank.
  - `POST /api/applications/submit/`: Submit a KYC application with file upload.
- **Database**: SQLite for local storage.
- **File Uploads**: Supports PDF, PNG, JPG uploads.
- **Admin Interface**: Accessible at `/admin/`.

## Prerequisites

- [Python 3.12](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)
- [Postman](https://www.postman.com/downloads/) (optional, for API testing)

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/safaricom-backend-django.git
   cd safaricom-backend-django
2. **create virual environment**
   python -m venv venv
.\venv\Scripts\activate  # On Windows
3.**install dependencies**
   pip install -r requirements.txt
   

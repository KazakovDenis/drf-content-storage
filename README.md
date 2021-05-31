# Content storage
![Python version](https://img.shields.io/badge/Python-3.8-blue)
![Django version](https://img.shields.io/badge/Django-3.2-yellowgreen)
![DRF version](https://img.shields.io/badge/DRF-3.12-orange)
![gunicorn version](https://img.shields.io/badge/gunicorn-20.1-yellow)
[![Build Status](https://travis-ci.com/KazakovDenis/dynamic-sitemap.svg?branch=master)](https://travis-ci.com/KazakovDenis/drf-content-storage)
[![codecov](https://codecov.io/gh/KazakovDenis/dynamic-sitemap/branch/master/graph/badge.svg)](https://codecov.io/gh/KazakovDenis/drf-content-storage)

## Demo
Run the service into 2 steps:
- rename `example.env` to `.env`
- execute `docker-compose up -d`

Demo data will be added automatically.
Then visit `http://0.0.0.0` with **admin / admin** credentials.
You can also use browsable API at `http://0.0.0.0/api/`.

## API usage
### Get page list
```bash
GET /api/pages/
```
  
### Get page details
```bash
GET /api/pages/<int:page_id>/
```
  
### Get content list
Contents are videos, audios and texts. To get necessary content use, for example:
```bash
GET /api/videos/
```
  
### Get content details
```bash
GET /api/videos/<int:content_id>/
```

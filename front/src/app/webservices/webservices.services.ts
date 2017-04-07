import { Component, OnInit, Injectable } from '@angular/core';
import { AuthenticationService } from '../authentication';
import { Router } from '@angular/router';
import { Http, Response } from '@angular/http';

@Injectable()
export class WebService {
  constructor(private authService: AuthenticationService) { }

  public getCollegesPerYear() {
    return this.authService.getResource('/api/exploration/colleges-per-year');
  }
}

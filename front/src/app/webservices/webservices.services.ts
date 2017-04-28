import { Component, OnInit, Injectable } from '@angular/core';
import { Http, Headers, Response, RequestOptions } from '@angular/http';
import { Router } from '@angular/router';

@Injectable()
export class WebService {
  constructor(private http: Http, private router: Router) { }
  public postResource(body: String, url: string) {
    let headers = new Headers();
    headers.append('Content-Type', 'application/json');
    let options = new RequestOptions({ headers });
    return this.http.post(url, body, options);
  }

  /**
   * Get resource to fetch data from server using an end point as `url`
   */
  public getResource(url: string) {
    return this.http.get(url);
  }
  public getCollegesPerYear() {
    return this.getResource('/api/exploration/colleges-per-year');
  }
}

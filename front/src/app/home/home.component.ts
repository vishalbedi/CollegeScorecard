import { Component, OnInit } from '@angular/core';
import { Response } from '@angular/http';
import { WebService } from '../webservices';
import { User }    from './User';
import { College } from './Colleges';
@Component({
  selector: 'home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css'],
  providers: [WebService]
})
export class HomeComponent  {
  public genders = ['Male', 'Female'];
  public regions = ['Far West', 'Great Lakes', 'Mid East', 'New England', 'Plains',
    'Rocky Mountains', 'Southeast', 'Southwest'];
  public model = new User('', 600, 600, 600, '', '');
  public submitted: boolean = false;
  public colleges = [];
  constructor(private webservice: WebService) { }
  public onSubmit() {
    this.webservice.postResource(JSON.stringify(this.model), '/api/analytics/get-college-list')
      .subscribe(
        (data) => this.handleData(data),
        console.log,
        () => console.log('got data')
      );
  }
  /**
   * Fetch the data from the python-flask backend
   */

   private handleData(data: Response) {
    if (data.status === 200) {
      let receivedData = data.json();
      for (let i = 1; i < receivedData.length; i++) {
        this.colleges.push(new College(receivedData[i][0], receivedData[i][1], receivedData[i][2],
          receivedData[i][3], receivedData[i][4]));
      }
      this.submitted = true;
    }
  }
}

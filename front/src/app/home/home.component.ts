import { Component, OnInit } from '@angular/core';
import { Response } from '@angular/http';
import { AuthenticationService } from '../authentication';
import { WebService } from '../webservices';
import { User }    from './User';

@Component({
  selector: 'home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css'],
  providers: [WebService, AuthenticationService]
})
export class HomeComponent implements OnInit {
  public genders = ['Male', 'Female'];
  public regions = ['Far West', 'Great Lakes', 'Mid East', 'New England', 'Plains',
    'Rocky Mountains', 'Southeast', 'Southwest'];
  public model = new User('', 600, 600, 600, '', '');
  public collegesCharOptions: any =  {
    chartType: 'ColumnChart',
    dataTable: [],
    options: {title: 'Colleges Per Year'}
  };
  constructor(private webservice: WebService) { }

  public ngOnInit() {
    this.getData();
  }

  public onSubmit() {
    console.log('submitted');
  }
  /**
   * Fetch the data from the python-flask backend
   */
  private getData() {
    this.webservice.getCollegesPerYear()
      .subscribe(
        (data) => this.handleData(data),
        console.log,
        () => console.log('got data')
      );
  }

   private handleData(data: Response) {
    if (data.status === 200) {
      let receivedData = data.json();
      this.collegesCharOptions.dataTable = receivedData;
    }
    console.log(this.collegesCharOptions.dataTable);
  }
}

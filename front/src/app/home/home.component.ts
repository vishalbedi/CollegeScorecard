import { Component, OnInit } from '@angular/core';
import { Response } from '@angular/http';
import { AuthenticationService } from '../authentication';
import { WebService } from '../webservices';

@Component({
  selector: 'home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css'],
  providers: [WebService, AuthenticationService]
})
export class HomeComponent implements OnInit {

  public collegesCharOptions: any =  {
    chartType: 'ColumnChart',
    dataTable: [],
    options: {title: 'Colleges Per Year'}
  };
  constructor(private webservice: WebService) { }

  public ngOnInit() {
    this.getData();
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

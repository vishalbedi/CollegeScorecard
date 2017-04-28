import { Component, OnInit } from '@angular/core';
import { Response } from '@angular/http';
import { WebService } from '../webservices';
import { User }    from './User';

@Component({
  selector: 'home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css'],
  providers: [WebService]
})
export class HomeComponent implements OnInit {
  public genders = ['Male', 'Female'];
  public regions = ['Far West', 'Great Lakes', 'Mid East', 'New England', 'Plains',
    'Rocky Mountains', 'Southeast', 'Southwest'];
  public model = new User('', 600, 600, 600, '', '');
  public submitted: boolean = false;
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
    this.submitted = true;
    this.webservice.postResource(JSON.stringify(this.model), '/somewhere').subscribe();
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

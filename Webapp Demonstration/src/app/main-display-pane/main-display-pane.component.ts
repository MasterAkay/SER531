import { Component, OnInit } from '@angular/core';
import {HttpClient} from '@angular/common/http';

@Component({
  selector: 'app-main-display-pane',
  templateUrl: './main-display-pane.component.html',
  styleUrls: ['./main-display-pane.component.css']
})
export class MainDisplayPaneComponent implements OnInit {

  key = '';
  templateQuestionId = '';
  data;
  queryResultToDisplay = '';
  constructor(private httpClient: HttpClient) {

  }

  ngOnInit(): void {
  }

  // https://jsonplaceholder.typicode.com/posts
  functionOnClickGo(): void {

    this.httpClient.get('http://127.0.0.1:5000/users', {
      params: {
        Key: this.key,
        Template_ques_id: this.templateQuestionId
      },
      observe: 'response'
    })
      .toPromise()
      .then(response => {

        this.data = response.body;
        this.displayTypeOfQuery(this.data.data);
        console.log(this.data);
      })
      .catch(console.log);
  }
  displayTypeOfQuery(templateId): void{
    if (templateId === 0) {
      this.queryResultToDisplay = 'Ask (ent-pred-obj)';
    } else if (templateId === 1) {
      this.queryResultToDisplay = 'Ask (ent-pred-obj1 . ent-pred-obj2)';
    }else if (templateId === 2) {
      this.queryResultToDisplay = 'Count Obj (ent-pred-obj)';
    }else if (templateId === 3){
      this.queryResultToDisplay = 'Count ent (ent-pred-obj)';
    }else if (templateId === 4){
      this.queryResultToDisplay = '?E is_a Type, ?E pred Obj  value. MAX/MIN (value)';
    }else if (templateId === 5){
      this.queryResultToDisplay = '?E is_a Type. ?E pred Obj. ?E-secondClause value. MAX (value)';
    }else if (templateId === 6){
      this.queryResultToDisplay = '?E is_a Type. ?E pred Obj. ?E-secondClause value. MIN (value)';
    }else if (templateId === 7){
      this.queryResultToDisplay = '(E pred F) prop ?value';
    }else if (templateId === 8){
      this.queryResultToDisplay = '(E pred ?Obj ) prop value';
    }else if (templateId === 9){
      this.queryResultToDisplay = 'select where (ent-pred-obj1 . ent-pred-obj2)';
    }else if (templateId === 10){
      this.queryResultToDisplay = '[]';
    }else if (templateId === 11){
      this.queryResultToDisplay = 'E REF ?F . ?F RFG G';
    }else if (templateId === 12){
      this.queryResultToDisplay = 'C RCD xD . xD RDE ?E';
    }else if (templateId === 13){
      this.queryResultToDisplay = 'E REF xF . xF RFG ?G';
    }else if (templateId === 14){
      this.queryResultToDisplay = 'ASK ?sbj ?pred ?obj filter ?obj = num';
    }else if (templateId === 15){
      this.queryResultToDisplay = '<?S P O ; ?S InstanceOf Type>';
    }else if (templateId === 16){
      this.queryResultToDisplay = '<S P ?O ; ?O instanceOf Type>';
    }else if (templateId === 17){
      this.queryResultToDisplay = '<?S P O ; ?S instanceOf Type ; contains word >';
    }else if (templateId === 18){
      this.queryResultToDisplay = '<?S P O ; ?S instanceOf Type ; starts with character >';
    }else if (templateId === 19){
      this.queryResultToDisplay = 'E REF ?F';
    }else if (templateId === 20) {
      this.queryResultToDisplay = '?D RDE E';
    }
    }
}

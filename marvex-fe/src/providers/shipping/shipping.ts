import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import 'rxjs/add/operator/map';

/*
  Generated class for the ShippingProvider provider.

  See https://angular.io/guide/dependency-injection for more info on providers
  and Angular DI.
*/
@Injectable()
export class ShippingProvider {

  baseurl: string;
  item_count: number;

  constructor(public http: HttpClient) {
    console.log('Hello ShippingProvider Provider');
    this.baseurl = "http://localhost:8000/shipping/"
    this.item_count = 10;
  }

  getList(page: number) {
    console.log("Getting page number " + page);
    return this.http.get(this.baseurl + "?offset=" + page * this.item_count + "&limit=" + this.item_count);
  }

  getData(number: number) {
    console.log("Getting data for shipping, " + number);
    return this.http.get(this.baseurl + number);
  }

  getPage(url: string) {
    return this.http.get(url);
  }
}

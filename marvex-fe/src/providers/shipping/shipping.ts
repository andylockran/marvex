import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

/*
  Generated class for the ShippingProvider provider.

  See https://angular.io/guide/dependency-injection for more info on providers
  and Angular DI.
*/
@Injectable()
export class ShippingProvider {

  baseurl: string;

  constructor(public http: HttpClient) {
    console.log('Hello ShippingProvider Provider');
    this.baseurl = "http://localhost:8000/shipping/"
  }

  getData(number) {
    console.log("Getting data for shipping, " + number);
    return this.http.get(this.baseurl + number)
//    .map(res => res.json());
  }
}

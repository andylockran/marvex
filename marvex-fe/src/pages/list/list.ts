import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams, LoadingController } from 'ionic-angular';
import { ShippingProvider } from '../../providers/shipping/shipping';

/**
 * Generated class for the ListPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage({
  name: 'ListPage',
  segment: 'list/:count'
})
@Component({
  selector: 'page-list',
  templateUrl: 'list.html',
  providers: [ShippingProvider]
})

export class ListPage {

  loading: any;
  count: number = 0;
  shiplist: any = [];

  constructor(
    public navCtrl: NavController, 
    public navParams: NavParams,
    private shippingProvider: ShippingProvider,
    private loadingCtrl: LoadingController
  ) {
    this.loading = this.loadingCtrl.create({
      content: '<ion-spinner ></ion-spinner>',
    });
    this.loading.present();
    this.navParams.get('count');
  }

  ionViewDidEnter() {
    console.log('ionViewDidLoad ListPage');
    this.getList(this.count);
  }

  getList(count: number) {
    this.shippingProvider.getList(count).subscribe(
      result => {
        console.log(result);
        this.shiplist = result;
      },
      err => {
        console.log("Error: "+err);
      },
      () => {
        console.log("Getdata completed.");
        this.loading.dismiss();
      }
    )
  } 

  debug() {
    console.log(this.shiplist);
  }

  loadCompany(fk_id) {
    this.navCtrl.push("ShippingPage", {'number': fk_id});
  }

  loadPrevious() {
    this.navCtrl.pop();
  } 

  loadNext() {
    var number = this.count+1;
    this.navCtrl.push(ListPage, { count: number})
  } 

  getPageNumber() {
    var total = Math.round(this.shiplist.count / 10);
    return total;
  }
}

import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams, LoadingController } from 'ionic-angular';
import { ShippingProvider } from '../../providers/shipping/shipping';

/**
 * Generated class for the ShippingPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage({
  name: 'ShippingPage',
  segment: 'shipping/:number'
}
)
@Component({
  selector: 'page-shipping',
  templateUrl: 'shipping.html',
  providers:[ShippingProvider]
})
export class ShippingPage {

  company: any;
  number: number;
  loading: any;

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
    this.number = this.navParams.get('number');
    console.log(this.number);
  }

  ionViewDidLoad() {
    console.log('ionViewDidLoad ShippingPage');
    this.getData();
  }

  getData() {
    this.shippingProvider.getData(this.number).subscribe(
      result => {
        console.log(result),
        this.company = result;
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

  getInfo() {
    console.log(this);
  }
}

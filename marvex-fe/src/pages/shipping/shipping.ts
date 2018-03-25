import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams, LoadingController } from 'ionic-angular';
import { ShippingProvider } from '../../providers/shipping/shipping';

/**
 * Generated class for the ShippingPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-shipping',
  templateUrl: 'shipping.html',
  providers:[ShippingProvider]
})
export class ShippingPage {

  fk_id: number;
  company_na: string;
  registered: string;
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
  }

  ionViewDidLoad() {
    console.log('ionViewDidLoad ShippingPage');
    this.getData(1);
  }

  getData(number) {
    this.shippingProvider.getData(number).subscribe(
      result => {
        console.log(result),
        this.company_na = result.company_na;
        this.fk_id = result.fk_id;
        this.registered = result.registered;
        this.nationalit = result.nationalit;
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

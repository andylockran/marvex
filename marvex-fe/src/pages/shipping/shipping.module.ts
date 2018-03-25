import { NgModule } from '@angular/core';
import { IonicPageModule } from 'ionic-angular';
import { ShippingPage } from './shipping';
import { HttpClientModule } from '@angular/common/http';
import { ShippingflagComponent } from '../../components/shippingflag/shippingflag';

@NgModule({
  declarations: [
    ShippingPage,
    ShippingflagComponent
  ],
  imports: [
    IonicPageModule.forChild(ShippingPage),
    HttpClientModule,
  ],
})
export class ShippingPageModule {}

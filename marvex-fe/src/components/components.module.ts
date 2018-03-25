import { NgModule } from '@angular/core';
import { CountryflagComponent } from './countryflag/countryflag';
import { ShippingflagComponent } from './shippingflag/shippingflag';
import { ShippingfunnelComponent } from './shippingfunnel/shippingfunnel';
@NgModule({
	declarations: [
    CountryflagComponent,
    ShippingflagComponent,
    ShippingfunnelComponent],
	imports: [],
	exports: [
    CountryflagComponent,
    ShippingflagComponent,
    ShippingfunnelComponent]
})
export class ComponentsModule {}

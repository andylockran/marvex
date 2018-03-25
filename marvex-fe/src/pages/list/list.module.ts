import { NgModule } from '@angular/core';
import { IonicPageModule } from 'ionic-angular';
import { ListPage } from './list';
import { CountryflagComponent } from '../../components/countryflag/countryflag';

@NgModule({
  declarations: [
    ListPage,
    CountryflagComponent
  ],
  imports: [
    IonicPageModule.forChild(ListPage),
  ],
})
export class ListPageModule {}

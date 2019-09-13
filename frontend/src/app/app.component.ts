import { Component, OnInit, OnDestroy } from '@angular/core';
import { Subscription } from 'rxjs';

import { PluginsApiService } from './plugins/plugins-api.service'
import { Plugin } from './plugins/plugin.model'


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit, OnDestroy {
  title = 'app';
  pluginsListSubs: Subscription;
  pluginsList: Plugin[];

  constructor(private pluginsApi: PluginsApiService) {

  }

  ngOnInit() {
    this.pluginsListSubs = this.pluginsApi
      .getPlugins()
      .subscribe(res => {
        this.pluginsList = res;
      },
      console.error
      );
  }

  ngOnDestroy() {
    this.pluginsListSubs.unsubscribe();
  }
}

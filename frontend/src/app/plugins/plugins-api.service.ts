// Third-party Imports
import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Observable } from 'rxjs';

// Custom Imports
import { API_URL } from '../env';
import { Plugin } from './plugin.model';

@Injectable()
export class PluginsApiService {
    constructor(private http: HttpClient) {

    }

    private static _handleError(err: HttpErrorResponse | any) {
        return Observable.throw(err.message || 'Error: Unable to complete request');
    }

    // GET list of public future events
    getPlugins(): Observable<Plugin[]> {
        return this.http.get<Plugin[]>(`${API_URL}/plugins`);
    }
}
import React, { Component } from "react";
import DashboardPage from './DashboardPage'
import { BrowserRouter as Router, Switch , Route, Link, Redirect} from "react-router-dom"; 

export default class HomePage extends Component{
    constructor(props){
        super(props);
    }

    render(){
        return (
        <Router>
            <Switch>
                <Route  path="/login"><p>Esta e a login</p></Route>
                <Route path ="/dashboard" component={DashboardPage} />
            </Switch>
        </Router>
        );
    }
}
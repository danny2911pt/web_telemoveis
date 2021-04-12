import React, { Component } from "react";
import { BrowserRouter as Router, Switch , Route, Link, Redirect} from "react-router-dom" 
import LoginPage from './LoginPage'
import TelemovelPage from './TelemovelPage'
import DashboardPage from './DashboardPage'

export default class HomePage extends Component{
    constructor(props){
        super(props);
    }

    render(){
        return (
        <Router>
            <Switch>
                <Route exact path="/"><p>Esta e a HomePage</p></Route>
                <Route path ="/login" component={LoginPage}/>
                <Route path ="/dashboard" component={DashboardPage} />
                <Route path ="/telemovel" component={TelemovelPage} />
            </Switch>
        </Router>
        );
    }
}
import React, { Component } from "react";
import TelemovelPage from './TelemovelPage'
import { BrowserRouter as Router, Switch , Route, Link, Redirect} from "react-router-dom";


export default class HomePage extends Component{
    constructor(props){
        super(props);
    }

    render(){
        return (
        <Router>
            <Switch>
                <Route exact path="/dashboard"><p>Esta e a DashboardPage</p></Route>
                <Route path ="/telemovel" component={TelemovelPage} />
            </Switch>
        </Router>
        );
    }
}
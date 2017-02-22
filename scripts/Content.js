import * as React from 'react';

import { Button } from './Button';
import { Socket } from './Socket';


export class Content extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'numbers': []
        };
    }

    componentDidMount() {
        Socket.on('all numbers', (data) => {
            this.setState({
                'numbers' : data['numbers'] ,
                // 'picture' : data['picture'] , 
                // 'name'    : data['name']
            });
        })
    }

    render() {
       
        let numbers = this.state.numbers.map(
            (n, index) => <li className="number-item" key={index}>{n}</li>
        );
        return (
            <div>
                <div
                    className="fb-login-button"
                    data-max-rows="1"
                    data-size="medium"
                    data-show-faces="false"
                    data-auto-logout-link="true">
                </div>
                <div
                    // className="g-signin2"
                    // data-theme="dark"
                    >
                </div>
                <h1>Project 2 Chat Box</h1>
                
                <Button />
                <ul className="brick">{numbers}</ul>
            </div>
        );
    }
}

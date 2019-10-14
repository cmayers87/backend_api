import React, { Component } from 'react'
import ReactDOM from 'react-dom'

// import Header from './layout/Header'
// import Block from './Block'
// import Footer from './layout/Footer'
// import Fac from './Facs'

class App extends Component {
    render() {
        return (
            <div>
                <h1>Django-React Base App</h1>
            </div>
        )
    }
}

ReactDOM.render(<App />, document.getElementById('app'))
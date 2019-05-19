import React from 'react';
import DestinationList from './destinations/DestinationList';


class App extends React.Component {
    state = {}
    render() {
        return (
            <div>
                <DestinationList />
            </div>
        );
    }
}

export default App;
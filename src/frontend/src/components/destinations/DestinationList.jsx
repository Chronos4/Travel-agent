import React from 'react';
import axios from 'axios';

class DestinationList extends React.Component {
    state = {
        data: []
    }

    onLoad = async (term) => {
        const response = await axios.get('http://localhost:8000/superapi/destinations/'
        );

        // console.log(response.data);
        this.setState({ data: response.data });
        console.log(this.state.data[0].unique_id)
    };

    componentDidMount() {
        this.onLoad();
    };

    render() {
        const list = this.state.data.map(item => {
            return item.unique_id
        });
        return (

            <div className="container text-center my-5">

                <h4>Active Destinations</h4>
                <hr />
                <div className="row ml-4">

                    <div className="col-lg-4 col-sm-12 col-md-6 my-3">
                        <div className="card" >


                            <div className="card-body">
                                <h5>Travel to</h5>
                                <h1></h1>
                                <h1>{list}</h1>
                            </div>
                        </div>
                    </div>

                </div>
                <h3>No active destinations!</h3>
            </div>

        );
    }
}

export default DestinationList;
var Showadvertcards = React.createClass({
    loadAdvertssFromServer: function() {
        console.log('getting data');
        $.ajax({
          url: '/getadverts',
          dataType: 'json',
          cache: false,
          success: function(data) {
            this.setState({data: data});
            //console.log(data);
          }.bind(this),
          error: function(xhr, status, err) {
            console.error(this.props.url, status, err.toString());
          }.bind(this)
        });
    },
    getInitialState: function() {
        console.log('initial state');
        return {data: []};
    },
    componentDidMount: function() {
        console.log('component mounted');
        this.loadAdvertssFromServer();
    },
    render: function(){
        return(
            <div>
                <Advertcards data={this.state.data} />
            </div>
        )
    }
});

var Advertcards = React.createClass({
    render: function(){
        console.log(this.props.data)
        var advertNodes = this.props.data.map(function(advert) {
          return (
            <Advertcard key={advert.id} id={advert.id} product={advert.product} campaign={advert.campaign} tvStations={advert.tvStations} radioStations={advert.radioStations} style={advert.style} />
          );
        });
        return (
          <div>
            {advertNodes}
          </div>
        );
    }
});


var Advertcard = React.createClass({
    getInitialState: function() {
        return {nxturl: "/editadvert?" + this.props.id, cls: "card " + this.props.style};
    },
    handleEdit: function(id) {
        document.location.href = this.state.nxturl;
    },
    render: function(){
        console.log(this.state.cls);
        return(
            <div className="row" key={this.props.id}>
                <div className="col-xs-12">
                    <div className={this.state.cls} >
                        <div className="card-block">
                            <div className="row center-block">
                                <div className="col-xs-2">
                                    <p className="card-text">{this.props.product}</p>
                                </div>
                                <div className="col-xs-5 vcenter">
                                    <p className="card-text text-nowrap">{this.props.campaign}</p>
                                </div>
                                <div className="col-xs-3 vcenter">
                                    <p className="card-text text-nowrap">{this.props.tvStations} TV / {this.props.radioStations} Radio</p>
                                </div>
                                <div className="col-xs-1">
                                    <a onClick={this.handleEdit.bind(this, this.props.id)} href="#"><i className="fa fa-pencil fa-fw">&nbsp;</i></a>
                                </div>
                                <div className="col-xs-1">
                                    <a href="#"><i className="fa fa-times">&nbsp;</i></a>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        )
    }
});


ReactDOM.render(
  <Showadvertcards />,
  document.getElementById('page_content')
);
var Showstationcards = React.createClass({
    loadStationsFromServer: function() {
        console.log('getting data');
        console.log(this.state.advertid);
        $.ajax({
          url: '/getadvertdetails?a='+this.state.advertid,
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
        return {advertid: $('#advertid').val(), data: []};
    },
    componentDidMount: function() {
        console.log('component mounted');
        this.loadStationsFromServer();
    },
    render: function(){
        return(
            <div>
                <Stationcards data={this.state.data} />
            </div>
        )
    }
});

var Stationcards = React.createClass({
    render: function(){
        console.log(this.props.data)
        var stationNodes = this.props.data.map(function(station) {
          return (
            <Stationcard key={station.station_id} station_id={station.station_id} campaign_id={station.campaign_id}
                                station_name={station.station_name} station_type_desc={station.station_type_desc}
                                station_type_id={station.station_type_id} schedule_dates={station.schedule_dates}
                                style={station.style} />
          );
        });
        return (
          <div>
            {stationNodes}
          </div>
        );
    }
});

var Stationcard = React.createClass({
    getInitialState: function() {
        return {station_id:this.props.station_id, campaign_id:this.props.campaign_id,
                station_name:this.props.station_name, station_type_desc:this.props.station_type_desc,
                station_type_id:this.props.station_type_id, schedule_dates:this.props.schedule_dates,
                cls: "card " + this.props.style, toltipid: "card-text-"+ this.props.station_id,
                tooltipdate: "sdates-"+ this.props.station_id};
    },
    showToolTip: function(){
        $('.tooltipd').tooltipster('hide')
        console.log('mouse over called')
        var tooltipdateholder = this.state.tooltipdate
        var sdates = this.state.schedule_dates.split(',').map(Function.prototype.call, String.prototype.trim)
        var tooltipid_ = this.state.toltipid
        $('#'+ tooltipid_).tooltipster('show', function() {
           $('#'+ tooltipdateholder).multiDatesPicker({
                dateFormat: "dd-mm-yy",
                addDates: sdates,
                beforeShowDay: function (date) {
                   if (date.getDate() >= 1 || date.getDate() <= 31) {
                       return [false, ''];
                   }
                }
           })
        })
    },
    hideToolTip: function(){
        var tooltipid_ = this.state.toltipid
        $('#'+ tooltipid_).tooltipster('hide')
    },
    componentDidMount: function() {
        var tooltipdateholder = this.state.tooltipdate
        $('#'+ this.state.toltipid).tooltipster({
            content: $('<div id='+tooltipdateholder+'></div>'),
	        position: 'left',
	        interactive: true,
	        trigger: 'custom'
        })
    },
    render: function(){
        console.log(this.state.cls);
        return(
            <div className="row" key={this.props.station_id}>
                <div className="col-xs-12">
                    <div className={this.state.cls} >
                        <div className="card-block">
                            <div className="row">
                                <div className="col-xs-4">
                                    <p className="card-title">{this.props.station_name}({this.props.station_type_desc})</p>
                                </div>
                                <div className="col-xs-6 vcenter tooltipd" id={this.state.toltipid}>
                                    <p className="card-text">{this.props.schedule_dates}<a href="#" onClick={this.showToolTip}>...&nbsp;<i className="fa fa-plus-square-o"></i></a></p>
                                </div>
                                <div className="col-xs-1">
                                    <a role="button" data-toggle="modal" data-backdrop="static" data-keyboard="false"
                                        data-target="#editScheduleModal" data-stationid={this.props.station_id}
                                        data-campaignid={this.props.campaign_id} data-stationname={this.props.station_name}
                                        data-scheduledates={this.props.schedule_dates}><i className="fa fa-pencil fa-fw">&nbsp;</i></a>
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
  <Showstationcards />,
  document.getElementById('page_content')
);
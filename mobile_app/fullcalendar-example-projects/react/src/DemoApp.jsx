import React from 'react'
import FullCalendar, { formatDate } from '@fullcalendar/react'
import dayGridPlugin from '@fullcalendar/daygrid'
import timeGridPlugin from '@fullcalendar/timegrid'
import interactionPlugin from '@fullcalendar/interaction'
import { INITIAL_EVENTS, createEventId } from './event-utils'
import './App.css'
import axios from "axios"
export default class DemoApp extends React.Component {
  constructor(props) {
    super(props)
  
    this.state = {
      weekendsVisible: true,
      currentEvents: [],
      calEvents:[],
      loading:false
    }
  }
  componentDidMount(){
    this.setState({...this.state,loading:true})
    axios.get("https://edmodo-automation.herokuapp.com/api/get_assignments")
    .then(res=>{
      // var res={}
      // res.data=[{"Date":"2021-31-10","assigns":[{"id":0,"start":"2021-31-10","title":" DBMS LAB-5AWeek 8 submission"},{"id":1,"start":"2021-31-10","title":"CNS_2021_Aug_DecLab - 5  Remote DNS cache Poisoning Attack Lab"}]},{"Date":"2021-03-11","assigns":[{"id":0,"start":"2021-03-11","title":"CNS_2021_Aug_DecAssignment - 6"}]},{"Date":"2021-14-11","assigns":[{"id":0,"start":"2021-14-11","title":"2021_Odd_CS301_DBMS_ADBMS Assignment-4"}]}]
      console.log("data",res)
      var Events=[]
      for(let i=0;i<res.data.length;i++){
        const element = res.data[i]
        Events.push(...element.assigns)
    }
    for(let i=0;i<Events.length;i++){
      const element=Events[i]
      var date=element.start
      var dateArray=date.split("-")
      var temp=dateArray[1]
      dateArray[1]=dateArray[2]
      dateArray[2]=temp
      element.start=dateArray.join("-")  
      console.log("eve",Events)
    }
    this.setState({...this.state,calEvents:Events,currentEvents:Events,loading:false})
    // console.log(Events)
    })
    .catch(err=>{console.log(err)})
    // const res.data=[{"Date":"10/31/2021","assigns":[{"Date":"10/31/2021","Group-name":" DBMS LAB-5A","Time":"11:59 PM","Title":"Week 8 submission"},{"Date":"10/31/2021","Group-name":"CNS_2021_Aug_Dec","Time":"11:59 PM","Title":"Lab - 5  Remote DNS cache Poisoning Attack Lab"}]},{"Date":"11/03/2021","assigns":[{"Date":"11/03/2021","Group-name":"CNS_2021_Aug_Dec","Time":"11:59 PM","Title":"Assignment - 6"}]},{"Date":"11/14/2021","assigns":[{"Date":"11/14/2021","Group-name":"2021_Odd_CS301_DBMS_A","Time":"11:59 PM","Title":"DBMS Assignment-4"}]}]
    
  }
  
  
  
  render() {
    const { loading } = this.state
    if(loading){
      return(<>Loading</>)
    }
    else{
    return (
      <div className='demo-app'>
        {/* {this.renderSidebar()} */}
        <div className='demo-app-main'>
          <button>Update</button>
          <FullCalendar
            plugins={[dayGridPlugin, timeGridPlugin, interactionPlugin]}
            headerToolbar={{
              left: 'prev,today,next',
              center: 'title',
              right: 'dayGridMonth'
            }}
            initialView='dayGridMonth'
            editable={true}
            selectable={true}
            selectMirror={true}
            dayMaxEvents={true}
            weekends={this.state.weekendsVisible}
            initialEvents={INITIAL_EVENTS}
            events={this.state.calEvents} // alternatively, use the `events` setting to fetch from a feed
            select={this.handleDateSelect}
            eventContent={renderEventContent} // custom render function
            eventClick={this.handleEventClick}
            eventsSet={this.handleEvents} // called after events are initialized/added/changed/removed
            /* you can update a remote database when these fire:
            eventAdd={function(){}}
            eventChange={function(){}}
            eventRemove={function(){}}
            */
          />
        </div>
      </div>
    )
          }
  }

  renderSidebar() {
    return (
      <div className='demo-app-sidebar'>
        <div className='demo-app-sidebar-section'>
          <h2>Instructions</h2>
          <ul>
            <li>Select dates and you will be prompted to create a new event</li>
            <li>Drag, drop, and resize events</li>
            <li>Click an event to delete it</li>
          </ul>
        </div>
        <div className='demo-app-sidebar-section'>
          <label>
            <input
              type='checkbox'
              checked={this.state.weekendsVisible}
              onChange={this.handleWeekendsToggle}
            ></input>
            toggle weekends
          </label>
        </div>
        <div className='demo-app-sidebar-section'>
          <h2>All Events ({this.state.currentEvents.length})</h2>
          <ul>
            {this.state.currentEvents.map(renderSidebarEvent)}
          </ul>
        </div>
      </div>
    )
  }

  handleWeekendsToggle = () => {
    this.setState({
      weekendsVisible: !this.state.weekendsVisible
    })
  }

  handleDateSelect = (selectInfo) => {
    let title = prompt('Please enter a new title for your event')
    let calendarApi = selectInfo.view.calendar

    calendarApi.unselect() // clear date selection

    if (title) {
      calendarApi.addEvent({
        id: createEventId(),
        title,
        start: selectInfo.startStr,
        end: selectInfo.endStr,
        allDay: selectInfo.allDay
      })
    }
  }

  handleEventClick = (clickInfo) => {
    if (confirm(`Are you sure you want to delete the event '${clickInfo.event.title}'`)) {
      clickInfo.event.remove()
    }
  }

  handleEvents = (events) => {
    this.setState({...this.state,
      currentEvents: events
    })
  }

}

function renderEventContent(eventInfo) {
  return (
    <>
      <b>{eventInfo.timeText}</b>
      <i>{eventInfo.event.title}</i>
    </>
  )
}

function renderSidebarEvent(event) {
  return (
    <li key={event.id}>
      <b>{formatDate(event.start, {year: 'numeric', month: 'short', day: 'numeric'})}</b>
      <i>{event.title}</i>
    </li>
  )
}

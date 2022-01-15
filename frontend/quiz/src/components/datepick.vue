<template>
  <div>
    <select v-model="value">
      <option disabled value="">Please select one</option>
      <option
        v-for="item in listname"
        v-bind:value="[
          item.InstructorCode,
          item.DisableDates,
          item.TimeStart,
          item.TimeEnd
        ]"
      >
        {{ item.FullName }}
      </option>
    </select>
    <br /><br />
    <date-picker
      v-model="date"
      valueType="format"
      :disabled-date="disableDates"
    ></date-picker>
    <button v-on:click="showTime">Search</button><br /><br />
    <h2>ช่วงเวลาที่พร้อม {{ value[2] }}-{{ value[3] }}</h2>
    <h3 v-for="item in time_notactive">
      เวลาที่โดนจองแล้ว {{ item.TimeStart }}-{{ item.TimeEnd }}
    </h3>
    <vue-timepicker v-model="time" format="HH"></vue-timepicker>
    <button v-on:click="save">save</button><br /><br />
  </div>
</template>

<script>
import axios from "axios";
import DatePicker from "vue2-datepicker";
import "vue2-datepicker/index.css";
import VueTimepicker from "vue2-timepicker";
import "vue2-timepicker/dist/VueTimepicker.css";

export default {
  components: { DatePicker, VueTimepicker },
  data() {
    return {
      time: null,
      date: null,
      listname: null,
      value: [],
      time_notactive: null,
      status: null
    };
  },
  created() {
    this.selctName();
  },
  methods: {
    save() {
      axios
        .post("http://localhost:5000/save", {
          code: this.value[0],
          date: this.date,
          time: this.time
        })
        .then(response => {
          this.status = response.data;
          console.log(this.status);
        });
    },
    showTime() {
      axios
        .post("http://localhost:5000/date", {
          code: this.value[0],
          date: this.date
        })
        .then(response => {
          this.time_notactive = response.data;
          console.log(this.time_notactive);
        });
    },
    selctName() {
      axios.get("http://localhost:5000/name").then(response => {
        this.listname = response.data;
        console.log(this.listname);
      });
    },
    disableDates(date) {
      var disable_time = this.value[1];
      const day = new Date(date).getDay();
      if (this.value[0] == "VD0002") {
        return day === 0 || day === 4 || day === 5 || day === 6;
      }
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>

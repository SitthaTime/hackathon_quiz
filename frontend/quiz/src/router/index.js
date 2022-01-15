import Vue from "vue";
import Router from "vue-router";
import datepick from "@/components/datepick";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: "/",
      name: "datepick",
      component: datepick
    }
  ]
});

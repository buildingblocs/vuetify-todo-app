<template>
  <v-container fluid>
    <v-card>
      <v-list two-line subheader>
                  <v-subheader class="headline">{{day}}, {{date}}{{ord}} {{year}}</v-subheader>
                  <p class="mx-12 text-right"><b>{{todos.length}}</b> Tasks</p>

                  <v-list-item>
                    <v-list-item-content>
                      <v-list-item-title>

                        <v-text-field v-model="newTodo" id="newTodo" name="newTodo" label="Type your Task." @keyup.enter="addTodo" />
                        <v-datetime-picker v-model="datetimeString"></v-datetime-picker>
                      </v-list-item-title>
                    </v-list-item-content>
                  </v-list-item>

                </v-list>

                <v-list subheader two-line flat>
                  <v-subheader class="subheading" v-if="todos.length == 0">You have 0 Tasks, add some</v-subheader>
                  <v-subheader class="subheading" v-else="todos.length == 1">Your Tasks</v-subheader>

                  <v-list-item-group>
                    <v-list-item v-for="(todo, i) in todos">
                      <template #default="{ active, toggle }">
                        <v-list-item-action>

                          <v-checkbox v-model="active" @click="toggle"></v-checkbox>
                        </v-list-item-action>

                        <v-list-item-content>
                          <v-list-item-title :class="{
                  done: active
                  }">{{ todo.title | capitalize }}</v-list-item-title>
                          <v-list-item-subtitle>Added on: {{ date }}{{ ord }} {{ day }} {{ year }}</v-list-item-subtitle>
                        </v-list-item-content>
                        <v-btn fab ripple small color="red" v-if="active" @click="removeTodo(i)">
                          <v-icon class="white--text">mdi-close</v-icon>
                        </v-btn>
                      </template>
                    </v-list-item>
                  </v-list-item-group>
                </v-list>
              </v-card>
  </v-container>
</template>

<script lang="ts">
import Vue from "vue";
import api from "@/api/github";
import {Repo} from "@/types/github";

export default Vue.extend({
  name: "Todo",
  data: function () {
    return {
      isDark: true,
      show: true,
      newTodo: "",
      todos: [],
      day: todoDay(),
      date: new Date().getDate(),
      ord: nth(new Date().getDate()),
      year: new Date().getFullYear()
    };
  },
  methods: {
    addTodo() {
      const value = this.newTodo && this.newTodo.trim();
      if (!value) {
        return;
      }

      this.todos.push({
        title: this.newTodo,
        done: false
      });
      this.newTodo = "";
    },

    removeTodo(index: number) {
      this.todos.splice(index, 1);
    },

    todoDay() {
      const date = new Date();
      const days = [
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday"
      ];
      return days[date.getDay()];
    },

    nth(d: number) {
      if (d > 3 && d < 21) return "th";
      switch (d % 10) {
        case 1:
          return "st";
        case 2:
          return "nd";
        case 3:
          return "rd";
        default:
          return "th";
      }
    }
  },

  filters: {
    capitalize: function (value: string) {
      if (!value) return "";
      return value.charAt(0).toUpperCase() + value.slice(1);
    }
  }
});

</script>

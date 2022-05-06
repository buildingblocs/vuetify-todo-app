<template>
  <v-container fluid>
    <v-card>
      <v-card-title>Welcome to the Demo</v-card-title>
      <div class="pa-8">
          <v-data-table :items="todos" :headers="table.headers">
          </v-data-table>
        </div>
    </v-card>
  </v-container>
</template>

<script lang="ts">
import Vue from "vue";
import Todo from "@/types/todo";
import {getTodos} from "@/api/own";

export default Vue.extend({
  name: "Demo",
  data: function() {
    return {
      name: "YourName",
      class: "504",
      todos: Array<Todo>(),
      table: {
        headers: [
          {text: "Title", value: "title"}
        ]
      }
    };
  },
  mounted() {
    this.todos = this.getAllTodos();
  },

  methods: {
    getAllTodos() {
      getTodos().then(todos => {
        this.$data.todos = todos;
      });
    }

  }
});
</script>

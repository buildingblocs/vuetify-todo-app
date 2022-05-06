<template>
  <v-container fluid>
    <v-card>
      <div class="pa-8">

        <v-row justify='center'>
          <v-col cols='auto' align-self="center">
            <v-text-field v-model="newTodo" label="New Todo" style="width: auto" v-on:keyup.enter="search" />
          </v-col>
          <v-col cols='auto' align-self="center">
            <v-btn v-on:click="addTodo" style="display: block; margin: auto">Add</v-btn>
          </v-col>
          <v-col cols='auto' align-self="center">
            <v-btn v-on:click="clearTodo" style="display: block; margin: auto">Clear</v-btn>
          </v-col>
          <v-col cols='auto' align-self="center">
            <v-btn v-on:click="reloadTodo" style="display: block; margin: auto">Reload</v-btn>
          </v-col>
        </v-row>
      <v-data-table :headers="table.headers" :items="todos">
    </v-data-table>
    </div>
              </v-card>
  </v-container>
</template>

<script lang="ts">
import Vue from "vue";
import {Todo} from "@/types/todo";
import {createTodo, getTodos, clearTodos} from "@/api/own";

export default Vue.extend({
  name: "Todo",
  data: function () {
    return {
      isDark: true,
      show: true,
      newTodo: "",
      todos: Array<Todo>(),
      table: {
        headers: [
          {
            text: "Complete?",
            value: "isDone"
          },
          {
            text: "Title",
            value: "title"
          },
        ]
      }
    };
  },
  methods: {
    async addTodo() {
      const value = this.newTodo && this.newTodo.trim();
      if (!value) {
        return;
      }

      await createTodo(this.newTodo);

      this.newTodo = "";

      this.reloadTodo();
    },

    async clearTodo() {
      await clearTodos();

      this.reloadTodo();
    },

    reloadTodo() {
      getTodos().then(todos => {
        this.$data.todos = todos;
      });
    }
  }  ,
  mounted() {
    this.reloadTodo();
  }
});

</script>

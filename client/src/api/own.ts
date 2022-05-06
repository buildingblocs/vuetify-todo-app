// This is the site of accessing our very own API

import {Todo} from "@/types/todo";
import axios from "axios";

export async function createTodo(title: string): Promise<null> {
  const data = await (await axios.post("/api/new_todo", {title: title})).data;
  return data;
}

export async function getTodos(): Promise<Todo[]> {
  try {
        const resp = await axios.get("/api/todos");
        return (await resp.data) as Todo[];
    } catch (err) {
        console.error(err);
        return [];
    }
}

export async function clearTodos(): Promise<null> {
  const data = await (await axios.post("/api/clear_todo")).data;
  return data;
}

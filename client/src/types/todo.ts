export class Quote {
  author!: string
  content!: string
  date!: Date

  constructor(author: string, content: string) {
    this.author = author;
    this.content  = content;
  }
}

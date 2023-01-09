
const alpineObjectBase = {
    hasError: false,
    blur(event) {
      this.validate(event.target)        
    },
    validate(element) {            
      field = this[element.name]
      let rules = JSON.parse(element.dataset.rules)

      field.errored = ! Iodine.assert(field.data, rules).valid
      this.hasError = field.errored    
    },
    submit(e) {
      let inputs = [...this.$el.querySelectorAll("input[data-rules]")];
      inputs.map((input) => {
        this.validate(input)
      });  

      if (this.hasError)
        return
                              
      e.target.submit()
    }
}
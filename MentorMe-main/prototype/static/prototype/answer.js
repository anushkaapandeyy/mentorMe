var answers = JSON.parse(document.getElementById("answers").textContent);
console.log(answers)
function Answered_Questions() {
    const [state, setState] = React.useState({
        answers: answers,
    })
    function goToForum(id){
        window.location.href = `/mentorme/forum/${id}`;
    }
    return (
        <div>
            
            {state.answers.map((answer) => (
                
                <Answer answer={answer} goToForum={() => goToForum(answer.answer_id)} />
            ))}
        </div>
    )
}
ReactDOM.render(<Answered_Questions />, document.querySelector("#similar_questions"));
function Answer(props){
    return (
        <div class="answer">
            <br></br>
            <div> {props.answer.title} </div>
            <button onClick={props.goToForum}>See Answer</button>
        </div>
    )
}
var questions = JSON.parse(document.getElementById("questions").textContent);

function Notification() {
    const [state, setState] = React.useState({
        questions: questions,
    })
    function answerQuestion(id){
        window.location.href = `/mentorme/answer/${id}`;
    }
    return (
        <div>
            {state.questions.map((question) => (
                
                <Question question={question} answerQuestion={() => answerQuestion(question.question_id)} />
            ))}
        </div>
    )
}
ReactDOM.render(<Notification />, document.querySelector("#notifications"));
function Question(props){
    return (
        <div class="question">
            {props.question.title}
            <button onClick={props.answerQuestion}>Answer</button>
        </div>
    )
}
import { useEffect, useState } from "react";

const API_URL = "http://127.0.0.1:8000/api/questions/"; // Настрой на свой бекенд

export default function App() {
  const [questions, setQuestions] = useState([]);

  useEffect(() => {
    fetch(API_URL)
      .then((res) => res.json())
      .then((data) => setQuestions(data));
  }, []);

  const vote = (choiceId) => {
    fetch(`${API_URL}vote/${choiceId}/`, { method: "POST" })
      .then((res) => res.json())
      .then((updatedChoice) => {
        setQuestions((prevQuestions) =>
          prevQuestions.map((q) => ({
            ...q,
            choices: q.choices.map((c) =>
              c.id === updatedChoice.id ? updatedChoice : c
            ),
          }))
        );
      });
  };

  return (
    <div className="p-4 max-w-2xl mx-auto">
      <h1 className="text-2xl font-bold mb-4">Опросы</h1>
      {questions.map((question) => (
        <div key={question.id} className="border p-4 rounded-lg mb-4">
          <h2 className="text-xl font-semibold">{question.question_text}</h2>
          <ul>
            {question.choices.map((choice) => (
              <li key={choice.id} className="flex justify-between items-center mt-2">
                <span>{choice.choice_text}</span>
                <button
                  className="bg-blue-500 text-white px-3 py-1 rounded"
                  onClick={() => vote(choice.id)}
                >
                  Голосовать ({choice.votes})
                </button>
              </li>
            ))}
          </ul>
        </div>
      ))}
    </div>
  );
}

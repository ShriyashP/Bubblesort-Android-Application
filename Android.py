import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity

class MainActivity : AppCompatActivity() {

    private lateinit var inputEditText: EditText
    private lateinit var sortButton: Button
    private lateinit var resultTextView: TextView

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        inputEditText = findViewById(R.id.inputEditText)
        sortButton = findViewById(R.id.sortButton)
        resultTextView = findViewById(R.id.resultTextView)

        sortButton.setOnClickListener {
            val input = inputEditText.text.toString()
            val numbers = input.split(",").map { it.trim().toInt() }.toIntArray()
            val sortedArray = bubbleSort(numbers)
            resultTextView.text = "Sorted Array: ${sortedArray.joinToString(", ")}"
        }
    }

    private fun bubbleSort(arr: IntArray): IntArray {
        val n = arr.size
        for (i in 0 until n - 1) {
            for (j in 0 until n - i - 1) {
                if (arr[j] > arr[j + 1]) {
                    // Swap elements
                    val temp = arr[j]
                    arr[j] = arr[j + 1]
                    arr[j + 1] = temp
                }
            }
        }
        return arr
    }
}

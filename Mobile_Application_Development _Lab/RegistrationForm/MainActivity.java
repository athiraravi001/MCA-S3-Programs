package com.example.registrationform;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.EditText;
import android.widget.RadioButton;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    // UI elements
    EditText name, username, email, pwd, designation, languages, dob;
    RadioButton btMale, btFemale, btOther;
    Button submit;
    CheckBox check;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Initialize views
        name = findViewById(R.id.rname);
        username = findViewById(R.id.runame);
        email = findViewById(R.id.remail);
        pwd = findViewById(R.id.rpswrd);
        designation = findViewById(R.id.rdesignation);
        btMale = findViewById(R.id.rmale);
        btFemale = findViewById(R.id.rfemale);
        btOther = findViewById(R.id.rother);
        languages = findViewById(R.id.rlanguages);
        dob = findViewById(R.id.rdob);
        submit = findViewById(R.id.btnRegister);
        check = findViewById(R.id.rcheck);

        // Set click listener for register button
        submit.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (checkAllFields()) {
                    Toast.makeText(MainActivity.this, "Registered Successfully!", Toast.LENGTH_SHORT).show();
                }
            }
        });
    }

    private boolean checkAllFields() {
        // Name validation
        if (name.getText().toString().trim().isEmpty()) {
            name.setError("Name is required");
            return false;
        }

        // Username validation
        String uname = username.getText().toString().trim();
        if (uname.isEmpty()) {
            username.setError("Username is required");
            return false;
        } else if (uname.length() < 6 || !uname.matches(".*[A-Za-z].*")) {
            username.setError("Username must be at least 6 characters and contain at least one alphabet");
            return false;
        }

        // Email validation
        if (email.getText().toString().trim().isEmpty()) {
            email.setError("Email is required");
            return false;
        } else {
            String e_mail = email.getText().toString();
            String checkemail = "[a-zA-Z0-9._-]+@[a-z]+\\.+[a-z]+";
            if (!e_mail.matches(checkemail)) {
                email.setError("Invalid Email");
                return false;
            }
        }

        // Password validation
        String pass = pwd.getText().toString().trim();
        if (pass.isEmpty()) {
            pwd.setError("Password is required");
            return false;
        } else if (pass.length() < 6 || !pass.matches(".*[A-Za-z].*") || !pass.matches(".*[0-9].*") || !pass.matches(".*[!@#$%^&*+=?-].*")) {
            pwd.setError("Password must include letters, numbers, and special characters, and be at least 6 characters long");
            return false;
        } //!pass.matches(".*[A-Z].*") || !pass.matches(".*[a-z].*")
          // else if (!pass.matches("^(?=.*[A-Za-z])(?=.*[0-9])(?=.*[!@#$%^&*+=?-]).{6,}$"))

        // Designation validation
        if (designation.getText().toString().trim().isEmpty()) {
            designation.setError("Designation is required");
            return false;
        }

        // Gender validation
        if (!btMale.isChecked() && !btFemale.isChecked() && !btOther.isChecked()) {
            Toast.makeText(this, "Please select gender", Toast.LENGTH_SHORT).show();
            return false;
        }

        // Languages known validation
        if (languages.getText().toString().trim().isEmpty()) {
            languages.setError("Please enter languages you know");
            return false;
        }

        // DOB validation
        String dobInput = dob.getText().toString().trim();
        if (dobInput.isEmpty()) {
            dob.setError("Date of Birth is required");
            return false;
        } else if (!dobInput.matches("^\\d{2}/\\d{2}/\\d{4}$")) {
            dob.setError("Enter DOB in DD/MM/YYYY format");
            return false;
        }

        // Checkbox validation
        if (!check.isChecked()) {
            check.setError("Please agree to Privacy Policy");
            check.requestFocus();
            return false;
        }

        return true; // All fields are valid
    }
}

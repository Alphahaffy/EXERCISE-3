//1
import java.time.*;
import java.util.*;

public class DateDifferenceCalculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("First date (YYYY-MM-DD): ");
        String date1String = scanner.nextLine();
        LocalDate date1 = LocalDate.parse(date1String, DateTimeFormatter.ISO_DATE);

        System.out.print("Second date (YYYY-MM-DD): ");
        String date2String = scanner.nextLine();
        LocalDate date2 = LocalDate.parse(date2String, DateTimeFormatter.ISO_DATE);

        long differenceInDays = ChronoUnit.DAYS.between(date1, date2);
        System.out.println("Difference in days: " + Math.abs(differenceInDays));
    }
}
//2
import java.util.Scanner;

public class TimeConversion {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter time in 24-hour format (HH:MM): ");
        String time24 = scanner.nextLine();

        String[] timeParts = time24.split(":");
        int hours = Integer.parseInt(timeParts[0]);
        int minutes = Integer.parseInt(timeParts[1]);

        String period;
        if (hours >= 12) {
            period = "PM";
            if (hours > 12) {
                hours -= 12;
            }
        } else {
            period = "AM";
            if (hours == 0) {
                hours = 12;
            }
        }

        System.out.println("Time in 12-hour format: " + hours + ":" + String.format("%02d", minutes) + " " + period);
    }
}
//3
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.time.temporal.ChronoUnit;
import java.util.Scanner;

public class AgeCalculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter your birth date (YYYY-MM-DD): ");
        String birthDateString = scanner.nextLine();
        LocalDate birthDate = LocalDate.parse(birthDateString, DateTimeFormatter.ISO_DATE);

        LocalDate currentDate = LocalDate.now();

        long ageInYears = ChronoUnit.YEARS.between(birthDate, currentDate);

        System.out.println("Your current age is: " + ageInYears + " years.");
    }
}
//3
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.time.temporal.ChronoUnit;
import java.util.Scanner;

public class AgeCalculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter your birth date (YYYY-MM-DD): ");
        String birthDateString = scanner.nextLine();
        LocalDate birthDate = LocalDate.parse(birthDateString, DateTimeFormatter.ISO_DATE);

        LocalDate currentDate = LocalDate.now();

        long ageInYears = ChronoUnit.YEARS.between(birthDate, currentDate);

        System.out.println("Your current age is: " + ageInYears + " years.");
    }
}


//4

import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.Scanner;
import java.time.format.DateTimeParseException;

public class DateParser {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter a date string in the format (YYYY-MM-DD): ");
        String dateString = scanner.nextLine();

        try {
            LocalDate date = LocalDate.parse(dateString, DateTimeFormatter.ISO_DATE);
            System.out.println("Parsed date: " + date);
        } catch (DateTimeParseException e) {
            System.out.println("Error parsing date: " + e.getMessage());
        }
    }
}



//5

import java.time.Duration;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.Scanner;

public class EventDurationCalculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the event start time (YYYY-MM-DD HH:mm): ");
        String startString = scanner.nextLine();
        LocalDateTime startTime = LocalDateTime.parse(startString, DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm"));

        System.out.print("Enter the event end time (YYYY-MM-DD HH:mm): ");
        String endString = scanner.nextLine();
        LocalDateTime endTime = LocalDateTime.parse(endString, DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm"));

        Duration duration = Duration.between(startTime, endTime);

        long hours = duration.toHours();
        long minutes = duration.minusHours(hours).toMinutes();

        System.out.println("Duration of the event: " + hours + " hours and " + minutes + " minutes.");
    }
}




//6


import java.time.*;
import java.time.format.DateTimeFormatter;
import java.util.Scanner;

public class TimeZoneConversion {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the date and time (YYYY-MM-DD HH:mm): ");
        String dateTimeString = scanner.nextLine();
        LocalDateTime dateTime = LocalDateTime.parse(dateTimeString, DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm"));

        System.out.print("Enter the source time zone (e.g., UTC): ");
        String sourceTimeZone = scanner.nextLine();
        ZoneId sourceZoneId = ZoneId.of(sourceTimeZone);

        System.out.print("Enter the target time zone (e.g., America/Los_Angeles): ");
        String targetTimeZone = scanner.nextLine();
        ZoneId targetZoneId = ZoneId.of(targetTimeZone);

        ZonedDateTime sourceDateTime = ZonedDateTime.of(dateTime, sourceZoneId);
        ZonedDateTime targetDateTime = sourceDateTime.withZoneSameInstant(targetZoneId);

        System.out.println("Converted date and time: " + targetDateTime.format(DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm z")));
    }
}




//7


import java.util.*;
import java.text.SimpleDateFormat;

class Reminder {
    Timer timer;

    public Reminder(Date remindDate, String message) {
        timer = new Timer();
        timer.schedule(new RemindTask(message), remindDate);
    }

    class RemindTask extends TimerTask {
        String message;

        public RemindTask(String message) {
            this.message = message;
        }

        public void run() {
            System.out.println("Reminder: " + message);
            timer.cancel(); // Terminate the timer thread
        }
    }
}

public class ReminderSystem {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the reminder date and time (YYYY-MM-DD HH:mm): ");
        String dateTimeString = scanner.nextLine();

        System.out.print("Enter the reminder message: ");
        String message = scanner.nextLine();

        try {
            SimpleDateFormat dateFormat = new SimpleDateFormat("yyyy-MM-dd HH:mm");
            Date remindDate = dateFormat.parse(dateTimeString);

            Reminder reminder = new Reminder(remindDate, message);
        } catch (Exception e) {
            System.out.println("Invalid date/time format. Please enter in the format YYYY-MM-DD HH:mm.");
        }
    }
}




//8

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.time.format.DateTimeParseException;
import java.time.temporal.ChronoUnit;
import java.util.Scanner;

public class DateTimeValidator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm");
        LocalDateTime currentDateTime = LocalDateTime.now();

        System.out.print("Enter a date and time in the format (YYYY-MM-DD HH:mm): ");
        String input = scanner.nextLine();

        try {
            LocalDateTime dateTime = LocalDateTime.parse(input, formatter);
            if (dateTime.isBefore(currentDateTime)) {
                System.out.println("Error: Please enter a future date and time.");
                return;
            }




//9

import java.time.LocalDate;
import java.time.Month;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class HolidayCalendar {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the year: ");
        int year = scanner.nextInt();

        Map<LocalDate, String> holidays = new HashMap<>();
        holidays.put(LocalDate.of(year, Month.JANUARY, 1), "New Year's Day");
        holidays.put(LocalDate.of(year, Month.FEBRUARY, 14), "Valentine's Day");
        holidays.put(LocalDate.of(year, Month.MAY, 1), "Labor Day");
        holidays.put(LocalDate.of(year, Month.JULY, 4), "Independence Day");
        holidays.put(LocalDate.of(year, Month.OCTOBER, 31), "Halloween");



//10



import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class PersonalCalendar {
    private static Map<LocalDateTime, String> events = new HashMap<>();
    private static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        while (true) {
            System.out.println("1. Add Event");
            System.out.println("2. Edit Event");
            System.out.println("3. Delete Event");
            System.out.println("4. View Calendar");
            System.out.println("5. Exit");
            System.out.print("Choose an option: ");
            int choice = scanner.nextInt();
            scanner.nextLine();  // Consume newline character

            switch (choice) {
                case 1:
                    addEvent();
                    break;
                case 2:
                    editEvent();
                    break;
                case 3:
                    deleteEvent();
                    break;
                case 4:
                    viewCalendar();
                    break;
                case 5:
                    System.out.println("Exiting...");
                    return;
                default:
                    System.out.println("Invalid choice. Please try again.");
            }
        }
    }

    private static void addEvent() {
        System.out.print("Enter event description: ");
        String description = scanner.nextLine();

        System.out.print("Enter event date and time (YYYY-MM-DD HH:mm): ");
        String dateTimeString = scanner.nextLine();
        LocalDateTime dateTime = LocalDateTime.parse(dateTimeString, DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm"));

        events.put(dateTime, description);
        System.out.println("Event added successfully.");
    }

    private static void editEvent() {
        System.out.print("Enter event date and time to edit (YYYY-MM-DD HH:mm): ");
        String dateTimeString = scanner.nextLine();
        LocalDateTime dateTime = LocalDateTime.parse(dateTimeString, DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm"));

        if (events.containsKey(dateTime)) {
            System.out.print("Enter new event description: ");
            String newDescription = scanner.nextLine();
            events.put(dateTime, newDescription);
            System.out.println("Event edited successfully.");
        } else {
            System.out.println("Event not found.");
        }
    }

    private static void deleteEvent() {
        System.out.print("Enter event date and time to delete (YYYY-MM-DD HH:mm): ");
        String dateTimeString = scanner.nextLine();
        LocalDateTime dateTime = LocalDateTime.parse(dateTimeString, DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm"));

        if (events.containsKey(dateTime)) {
            events.remove(dateTime);
            System.out.println("Event deleted successfully.");
        } else {
            System.out.println("Event not found.");
        }
    }

    private static void viewCalendar() {
        System.out.println("Your Calendar:");
        if (events.isEmpty()) {
            System.out.println("No events scheduled.");
        } else {
            for (Map.Entry<LocalDateTime, String> entry : events.entrySet()) {
                LocalDateTime dateTime = entry.getKey();
                String description = entry.getValue();
                System.out.println(dateTime.format(DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm")) + " - " + description);
            }
        }
    }
}

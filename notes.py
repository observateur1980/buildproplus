
        print("staus id: " + str(status_id))
        print("customer id " + str(customer_id))


        # if customer_id == 1:
        #     qs_projects.filter(Q(status__id=status_id) & Q(customer__id__gt=1))
        #     print("burda1")
        # else:
        #     qs_projects.filter(Q(status__id=status_id) & Q(customer__id=customer_id))
        #     print("burda2")

        # if customer_id == 1:
        #     qs_projects.filter(status__id=status_id).filter(customer__id__gt=1)
        #     print(qs_projects)
        # else:
        #     qs_projects.filter(Q(status__id=status_id) & Q(customer__id=customer_id))
        #     print(qs_projects)


        print("***********************************************")
        print(qs_projects)
        print("***********************************************")



            <div class="form-floating mb-3">
                <input class="form-control" id="email" type="email" placeholder="name@example.com" data-sb-validations="required,email" />
                <label for="email">Email address</label>
                <div class="invalid-feedback" data-sb-feedback="email:required">An email is required.</div>
                <div class="invalid-feedback" data-sb-feedback="email:email">Email is not valid.</div>
            </div>